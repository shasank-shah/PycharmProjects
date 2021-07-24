#!/usr/bin/env perl

use 5.032;
use warnings;
use feature 'signatures';
no warnings 'experimental::signatures';

sub zero_one ($i, $iterations = 30, $string = '') {
  (my $tmp = reverse $string) =~ tr/01/10/;
  $string .= '0' . $tmp;
  say "S$i: \"$string\"" if $ENV{DEBUG};
  return $string if $i == $iterations;
  return zero_one(++$i, $iterations, $string);
}

say zero_one(1, $ARGV[0]);


__DATA__

TASK #2 › 0/1 String
Submitted by: Mohammad S Anwar

A 0/1 string is a string in which every character is either 0 or 1.

Write a script to perform switch and reverse to generate S30 as described below:

switch:

Every 0 becomes 1 and every 1 becomes 0. For example, “101” becomes “010”.

reverse:

The string is reversed. For example, "001” becomes “100”.


UPDATE (2020-07-13 17:00:00):

It was brought to my notice that generating S1000 string would be nearly impossible. So I have decided to lower it down to S30. Please follow the rule as below:

S0 = “”
S1 = “0”
S2 = “001”
S3 = “0010011”
…
SN = SN-1 + “0” + switch(reverse(SN-1))

