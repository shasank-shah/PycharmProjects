#!/usr/bin/env perl
# -*- Mode: cperl; cperl-indent-level:4 tab-width: 8; indent-tabs-mode: nil -*-
# -*- coding: utf-8 -*-

=pod Word Search (No Options Vesion)

=head1 Usage

perl ch-2.pl <word search grid file path> <dictionary file path>

=head1 Solution

#. assumption: dictionary already stored in ascending order.
#  --> this was wrong assumption: I changed the subroutine accordingly.

1. store every possible words in every direction into array (and sorted)
   this words has possibly quite a huge amount of sub sequences
   but I guess the list of words in dictionary could be larger than ones
   in the grid.

2. compare against the dictionary

=head1 Comment

this was really heavier solution than I thought it would be.
5th Sep 2020: change some array -> array ref. to speed up little bit.

=cut

use strict; use warnings;
use v5.14; # say;

use Getopt::Long qw(:config gnu_compat);
use Pod::Usage;
use List::MoreUtils qw(uniq);
use File::Spec;
use FindBin;
use lib ( $FindBin::Bin );

use CombinationsIndex qw(combinationsIndex);

BEGIN {
    sub fs { "File::Spec" }
    $::debugging = 0;

    my $help = 0;

    GetOptions( "debug"   => \$::debugging,
                "grid=s"  => \$::gridPath,
                "dict=s"  => \$::dictPath,
                "help"    => \$help,
        ) or pod2usage(2);

    pod2usage( -exitval => 0, -verbose => 2 ) if $help;


    our $dprint = sub( @ ) {
        ++$|;
        print @_;
    };

    *::dprint = $::debugging ? $dprint : sub {};
}

# solution ... a long solution ...
# all the directions in a linear form
sub allColumnIndices ($$) {
    my ( $maxPos, $lineLen ) = @_;
    ( $lineLen == 0 ) and ( warn ( "line number is zero!!!" ), return () );
    my $rowsIdx = int $maxPos / $lineLen;
    map { my $c = $_;
          [ map { my $p = $c + $lineLen * $_;
                  $p > $maxPos ? () : $p } 0 .. $rowsIdx ] } 0 .. $lineLen -1
}

sub allRowIndices ($$) {
    my ( $maxPos, $lineLen ) = @_;
    my $rowsIdx = int $maxPos / $lineLen;
    map { my $r = $_ * $lineLen;
          [ map { my $p = $r + $_;
                  $p > $maxPos ? () : $p } 0 .. $lineLen - 1 ] } 0 .. $rowsIdx
}

sub allTopLeftToBottomRightIndices ($$) {
    my ( $maxPos, $lineLen ) = @_;
    my $rowsIdx = int $maxPos / $lineLen;
    map { my $b = $_;
          my $col = $b % $lineLen;
          [ $b, map {
              my $p = $b + $_;
              ( ($p <= $maxPos) # new position not exceed maximum pos(index)
                and (($p % $lineLen) > $col) ) # 3 -> 9 -> 15(X)
                ? $p : ()
            } (map {$_*($lineLen+1)} 1 .. $lineLen -1 ) ] }
      ( 0 .. ($lineLen -1), map { $lineLen*$_ } 1 .. $rowsIdx )
      # for every starting point
      # ( 0 .. 4 ),        ( 5, 10, 15 )
}

#  0  1  2  3  4
#  5  6  7  8  9   -> example for above and below
# 10 11 12 13 14
# 15 16 17

sub allTopRightToBottomLeftIndices ($$) {
    my ( $maxPos, $lineLen ) = @_;
    my $rowsIdx = int $maxPos / $lineLen;

    map { my $b = $_;
          my $col = $b % $lineLen;
          [ $b, map {
              my $p = $b + $_;
              ( ($p <= $maxPos)
                and (($p % $lineLen) < $col) ) # 2 -> 6 -> 10 -> 14(X)
                ? $p: ()
            } (map {$_*($lineLen-1)} 1 .. $col) ] }
      ( 0 .. ($lineLen -1), map { $lineLen*$_ -1 } 2 .. $rowsIdx+1 )
      # for every starting point
      # ( 0 .. 4 ),         ( 9, 14 )
}

sub allIndices ($$) { # summary of directions shown above
    my ( $maxPos, $lineLen ) = @_;
    map { $_->( $maxPos, $lineLen ) }
      \&allColumnIndices, \&allRowIndices,
      \&allTopLeftToBottomRightIndices,\&allTopRightToBottomLeftIndices;
}

sub bothDirection {
    ( @_ == 1 ) and return [@_]; # reversing one element not useful
    return [@_], [reverse @_];
}

sub subsequences {
    # if the length of dictionary is short, we don't actually need to
    # make subsequences because we can compare the words in dictionary
    # against a whole possible line. but... my dictionary contains 127,466 lines
    ( @_ == 1 ) and return [ @_ ];

    (map {[$_]} @_), # : combinations 1 out of @_
      map{ [ @_[ $$_[0] .. $$_[1] ] ] } combinationsIndex(2, scalar@_)
}

sub allSubsequencesIndices { # final summary of indices
    my ( $maxPos, $lineLen ) = @_;
    map { subsequences @$_ }
      map { bothDirection @$_ } allIndices( $maxPos, $lineLen );
}

sub genWordsOrganized {
    my ( $maxPos, $lineLen, $gridString ) = @_;
    my @gridChars = split "", $gridString;

    ::dprint "[DBG] the grid string (in lower case):\n$gridString\n\n";
    local $" = '';
    sort(
         uniq( map { "@gridChars[@$_]" }
               allSubsequencesIndices( $maxPos, $lineLen ) ) );
}

sub unsafe_slurpFile { # unsafe means can throw exception(die)
    my $FilePath = shift;
    -r $FilePath or ::dprint( "[ERR] $FilePath: not readable: bye!\n" );

    open( my $fh, '<', $FilePath ) or
        die "could not open chaos: $FilePath";

    local $/ = undef;
    my $data = <$fh>;
    close $fh;
    $data
}

sub prepareGridData ($) {
    my $gdata = shift; # raw data
    $gdata =~ s/ *//g;
    my $lineLen = index $gdata, $/;
    $gdata =~ s/\n//g;
    my $maxPos = (length $gdata) -1;

    $maxPos, $lineLen, (lc $gdata) # final $gdata is in a linear form
}

sub grepMatchedWordsRefWithSortedDataRef {
    my $dictWordsRef = $_[0];
    my $gridWordsRef = $_[1];

    my ( $di, $gi ) = ( 0, 0 );
    my @result;
    while ( $di < @$dictWordsRef and $gi < @$gridWordsRef ) {
        ::dprint "$$dictWordsRef[$di] vs $$gridWordsRef[$gi]\n";

        my $cmp = (lc $$dictWordsRef[$di]) cmp $$gridWordsRef[$gi];
        if ( $cmp == -1 ) { ++$di }
        elsif ( $cmp == 0 ) {
            push @result, $$dictWordsRef[$di];
            ++$di, ++$gi;
        }
        else { ++$gi }
    }
    \@result;
}

sub raku_arrayref { "[".(join ", ", @{$_[0]})."]" }

# testing ...
package main;

if ( not defined $::dictPath ) {
    #$::dictPath  //= fs->catfile( $FindBin::Bin, qw(.. data tinyDict.txt) );
    $::dictPath = '/usr/share/dict/words';
    ::dprint "[WRN] using default dictionary file: $::dictPath\n";
}

if ( not defined $::gridPath ) {
    $::gridPath  = fs->catfile( $FindBin::Bin, qw(.. data grid.txt) );
    ::dprint "[WRN] using default word grid search file: $::gridPath\n";
}

my $dictData    = unsafe_slurpFile( $::dictPath );
my $rawGridData = unsafe_slurpFile( $::gridPath );

my @dictOrganized = sort { (lc $a) cmp (lc $b) } ( split "\n", $dictData );
my @gridWordsOrganized = genWordsOrganized( prepareGridData( $rawGridData ) );

if ( $::debugging ) {
    my $cnt = scalar @gridWordsOrganized;
    ::dprint "[DBG] Total $cnt possible words in the word-search grid.\n";
    my $wd = length $cnt; # for fixed length of count
    my $i = 0;
    ::dprint(sprintf("%${wd}d  ",++$i), $_, $/) for @gridWordsOrganized;
}

my $matchedWords =
  grepMatchedWordsRefWithSortedDataRef( \@dictOrganized, \@gridWordsOrganized );

say "Word Search Grid:\n$rawGridData";
say "Total: ".(scalar @$matchedWords)." word(s) found.";
say raku_arrayref( $matchedWords );
