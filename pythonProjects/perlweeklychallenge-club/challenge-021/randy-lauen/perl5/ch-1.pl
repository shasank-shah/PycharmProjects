#!/usr/bin/env perl

use v5.28;
use strict;
use warnings;

=head1 SYNOPSIS

Task: Write a script to calculate the value of e, also known as Euler’s number and Napier’s constant.

In addition to calculating it myself, I took a tour through some of the CPAN modules that 
do it for you. Some modules, like Math::Pari, have a function called Euler() that returns
Euler's constant, which is not the same as Euler's number.

Example output:
    $ perl ch-1.pl
    +------------------------------+-----------------------------------------------------+
    | Module                       | Euler's Number                                      |
    +------------------------------+-----------------------------------------------------+
    | Math::Big::euler             | 2.7182818284590452353602874713526624977572470937    |
    | Math::NumberCruncher::ECONST | 2.7182818284590452353602874713526624977572470937    |
    | Math::NumberCruncher::_e_    | 2.7182818284590452353602874713526624977572470936... |
    | Math::Symbolic::EULER        | 2.71828182845905                                    |
    | Math::AnyNum::euler          | 2.7182818284590452353602874713526624977572470937    |
    | Sidef Number.e               | 2.7182818284590452353602874713526624977572470937    |
    | bigrat::e                    | 2.718281828459045235360287471352662497757           |
    | Calculated e                 | 2.7182818284590452353602874713526625112110646491... |
    +------------------------------+-----------------------------------------------------+

=cut

use Math::Big ();
use Math::BigFloat ();
use Math::NumberCruncher ();
use Math::Symbolic ();
use Math::AnyNum ();
use Sidef ();
use Text::Table::Tiny ();

my @eulers = (
    [ 'Math::Big::euler',              sub { Math::Big::euler(1, 47) } ],
    [ 'Math::NumberCruncher::ECONST',  sub { Math::NumberCruncher::ECONST( 46 ) } ],
    [ 'Math::NumberCruncher::_e_',     sub { substr( $Math::NumberCruncher::_e_, 0, 48 ) . '...' } ],
    [ 'Math::Symbolic::EULER',         sub { Math::Symbolic::EULER } ],
    [ 'Math::AnyNum::euler',           sub { Math::AnyNum->e } ],
    [ 'Sidef Number.e',                sub { Sidef->new()->execute_code("Number.e()") } ],
    [ 'bigrat::e',                     sub { require bigrat; bigrat::e() } ],
    # My calculated version of e starts to differ around the 35th decimal.
    [ 'Calculated e',                  sub { substr( e(), 0, 48 ) . '...'  } ],
);

my @table = [ 'Module', q{Euler's Number} ];
foreach my $euler ( @eulers ) {
    push @table, [ $euler->[0], $euler->[1]->() ];
}

say Text::Table::Tiny::generate_table( header_row => 1, rows => \@table );

exit 0;


sub e {
    my $e = Math::BigFloat->bzero;
    for my $n ( 0 .. 50 ) {
        $e += Math::BigFloat->bone / Math::BigFloat->new( factorial( $n ) );
    }
    return $e;
}


sub factorial {
    my $n = shift;
    return 1 if $n == 0;
    return $n * factorial( $n - 1 );
}

