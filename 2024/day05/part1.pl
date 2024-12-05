#!/usr/bin/perl
use strict;
use warnings;

use List::Util 'any';

sub part1 {
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

    for my $i ( $rules + 1 .. $#puzzle_input ) {
        my $line        = $puzzle_input[$i];
        my @pages       = split /,/sxm, $line;
        my $right_order = 1;

        for my $j ( 1 .. $#pages ) {

            for my $k ( 0 .. $j - 1 ) {
                if ( any { $pages[$k] eq $_ } @{ $before{ $pages[$j] } } ) {
                    $right_order = 0;
                    last;
                }
            }

            for my $k ( $j + 1 .. $#pages ) {
                if ( any { $pages[$k] eq $_ } @{ $after{ $pages[$j] } } ) {
                    $right_order = 0;
                    last;
                }
            }
        }

        if ($right_order) {
            $result += $pages[ ( scalar @pages / 2 ) ];
        }
    }

    return $result;
}

1;
