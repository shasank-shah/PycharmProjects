#!/usr/bin/perl

# For multiplication, the asterisk must be escaped \*.

use strict;

my $input = join( " ", @ARGV );

if ( $input !~ /.*?([IVXLCDM]+)(.*?)([IVXLCDM]+)/ ) { die "Invalid input" }
my $number1  = $1;
my $operator = $2;
my $number2  = $3;
$operator =~ s/[^\+\-\*\/]//g;

if ( $operator eq '+' ) {
    print dec2rom( rom2dec($number1) + rom2dec($number2) );
}
elsif ( $operator eq '-' ) {
    print dec2rom( rom2dec($number1) - rom2dec($number2) );
}
elsif ( $operator eq '*' ) {
    print dec2rom( rom2dec($number1) * rom2dec($number2) );
}
elsif ( $operator eq '/' ) {
    print dec2rom( int( rom2dec($number1) / rom2dec($number2) + .5 ) );
}
else { die "Invalid operator" }
print "\n";

sub dec2rom {
    my @rdb = qw(I IV V IX X  XL L  XC C   CD  D   CM  M);
    my @ddb = qw(1 4  5 9  10 40 50 90 100 400 500 900 1000);
    my $dec = $_[0];
    my $rom;
    for ( my $x = $#ddb ; $x >= 0 ; $x-- ) {
        if ( $dec / $ddb[$x] >= 1 ) {
            $rom .= $rdb[$x] x int( $dec / $ddb[$x] );
            $dec = $dec - ( $ddb[$x] * int( $dec / $ddb[$x] ) );
        }
    }
    return $rom;
}

sub rom2dec {
    my %r2d = (
        "I" => 1,
        "V" => 5,
        "X" => 10,
        "L" => 50,
        "C" => 100,
        "D" => 500,
        "M" => 1000
    );
    my $dec;
    my @char = split //, $_[0];
    for ( my $x = 0 ; $x <= $#char ; $x++ ) {
        my $current   = $r2d{ $char[$x] };
        my $lookahead = $r2d{ $char[ $x + 1 ] };
        if ( $lookahead > $current ) {
            $dec += $lookahead - $current;
            $x++;
        }
        else {
            $dec += $current;
        }
    }
    return $dec;
}
