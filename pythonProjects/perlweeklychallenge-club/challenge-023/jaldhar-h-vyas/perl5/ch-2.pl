#!/usr/bin/perl
use warnings;
use strict;
use 5.010;

sub isPrime {
    my ($n) = @_;

    if ($n < 2) {
        return undef;
    }

    if ($n == 2) {
        return 1;
    }

    for my $i (2 .. sqrt($n)) {
        if ($n % $i == 0) {
            return undef;
        }
    }

    return 1;
}

sub nextPrime {
    state $i = 1;
    if (scalar @_) {
        $i = shift;
    }

    while ($i++) {
        if (isPrime($i)) {
            return $i;
        }
    }
}

sub factorize {
    my ($n, $primeFactors) = @_;
    if ($n < 2) {
        return;
    }

    my $p = nextPrime(1);
    while ($p <= $n) {

        if ($n % $p == 0) {
            push @{$primeFactors}, $p;
            factorize($n / $p, $primeFactors);
        }
        $p = nextPrime();
    }
}

my $n = shift;

if ($n < 4) {
    die "Number must be greater than 3.\n";
}

my @primeFactors;
if (isPrime($n)) {
    push @primeFactors, $n;
} else {
    factorize($n, \@primeFactors);
}

say join q{, }, @primeFactors;
