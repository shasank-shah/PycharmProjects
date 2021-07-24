#!/usr/bin/perl -w
use strict;
use warnings;
use v5.26;
use DDP;
# TASK #2 � Smallest Neighbour
# Submitted by: Mohammad S Anwar
# You are given an array of integers @A.
# Write a script to create an array that represents the smallest element to the left of each corresponding index. If none found then use 0.

# Example 1
# Input: @A = (7, 8, 3, 12, 10)
# Output: (0, 7, 0, 3, 3)

# For index 0, the smallest number to the left of $A[0] is none, so we put 0.
# For index 1, the smallest number to the left of $A[1] in (7), is 7 so we put 7.
# For index 2, the smallest number to the left of $A[2] in (7, 8) is none, so we put 0.
# For index 3, the smallest number to the left of $A[3] in (7, 8, 3) is 3, so we put 3.
# For index 4, the smallest number to the left of $A[4] is (7, 8, 3, 12) is 3, so we put 3 again.

# Example 2
# Input: @A = (4, 6, 5)
# Output: (0, 4, 4)

# For index 0, the smallest number to the left of $A[0] is none, so we put 0.
# For index 1, the smallest number to the left of $A[1] in (4) is 4, so we put 4.
# For index 2, the smallest number to the left of $A[2] in (4, 6) is 4, so we put 4 again.