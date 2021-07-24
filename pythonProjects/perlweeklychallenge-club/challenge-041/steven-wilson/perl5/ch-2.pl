#!/usr/bin/env perl
# Author: Steven Wilson
# Date: 2020-01-02
# Week: 041
# Task #2
# Write a script to display first 20 Leonardo Numbers. Please checkout wiki page for more information.
# For example:

# L(0) = 1
# L(1) = 1
# L(2) = L(0) + L(1) + 1 = 3
# L(3) = L(1) + L(2) + 1 = 5
# and so on.
# https://en.wikipedia.org/wiki/Leonardo_number

use strict;
use warnings;

my @leonardo_numbers = ( 1, 1 );
my $counter = 2;

while ( $counter < 20 ) {
    $leonardo_numbers[$counter] =
        $leonardo_numbers[ $counter - 1 ] +
        $leonardo_numbers[ $counter - 2 ] +
        1;
    $counter++;
}

print join " ", @leonardo_numbers, "\n";
