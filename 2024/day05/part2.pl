#!/usr/bin/perl
use strict;
use warnings;

use List::Util 'any';

sub part2 {
    my @puzzle_input = @_;
    my $result       = 0;
    my $rules        = 0;
    my %before       = ();
    my %after        = ();

    chomp @puzzle_input;

    for my $line (@puzzle_input) {
        if ( $line eq q{} ) {
            last;
        }
        my @pages = split /[|]/sxm, $line;
        push @{ $before{ $pages[0] } }, $pages[1];
        push @{ $after{ $pages[1] } },  $pages[0];
        $rules++;
    }

    for my $i ( $rules + 1 .. scalar @puzzle_input - 1 ) {
        my $line  = $puzzle_input[$i];
        my @pages = split /,/sxm, $line;

        my @sorted_pages =
          sort {    ## no critic (BuiltinFunctions::ProhibitReverseSortBlock)
            return ( any { $a eq $_ } @{ $before{$b} } )
              || ( any { $b eq $_ } @{ $after{$a} } )
              ? 1
              : -1;
          } @pages;

        my $sorted = 1;
        for my $i ( 0 .. $#sorted_pages ) {
            if ( $sorted_pages[$i] ne $pages[$i] ) {
                $sorted = 0;
                last;
            }
        }

        if ( $sorted == 0 ) {
            $result += $sorted_pages[ ( scalar @sorted_pages / 2 ) ];
        }

    }

    return $result;
}

1;

