#!/usr/bin/env perl

# Using only the official postal (2-letter) abbreviations for the 50
# U.S. states, write a script to find the longest English word you can spell?
# Here is the list of U.S. states abbreviations as per wikipedia page
# (https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations). This
# challenge was proposed by team member Neil Bowers.

# This version prints all the largest words.

use 5.026;
use strict;
use autodie;
use warnings;
use Locale::US;
use List::Util qw(all);

my @postal_codes = Locale::US->new()->all_state_codes();
my %postal_codes = map {lc($_) => undef} @postal_codes;

my $largest_length_so_far = 0;
my @largest_words_so_far;

open my $dict, '<', '/usr/share/dict/words';
while (<$dict>) {
    chomp;
    my $word = $_;
    next unless length($word) >= $largest_length_so_far;
    next unless (length($word) % 2) == 0;
    next unless all {exists $postal_codes{$_}} (lc($word) =~ m/../g);
    if (length($word) == $largest_length_so_far) {
        push @largest_words_so_far, $word;
    } else {
        $largest_length_so_far = length($word);
        @largest_words_so_far = ($word);
    }
}
close $dict;

say foreach @largest_words_so_far;
