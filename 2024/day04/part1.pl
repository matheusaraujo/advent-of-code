#!/usr/bin/perl
use strict;
use warnings;

use Readonly;

Readonly my @XMAS       => qw( X M A S );
Readonly my @DIRECTIONS => (
    [ -1, -1 ], [ -1, 0 ],  [ -1, 1 ], [ 0, -1 ],
    [ 0,  1 ],  [ 1,  -1 ], [ 1,  0 ], [ 1, 1 ],
);

sub part1 {
    my @puzzle_input = @_;
    my @word_search  = parse_input(@puzzle_input);
    my ( $rows, $cols ) = ( scalar @word_search, scalar @{ $word_search[0] } );

    my $result = 0;
    for my $row ( 0 .. $rows - 1 ) {
        for my $col ( 0 .. $cols - 1 ) {
            $result +=
              count_word_occurrences( \@word_search, $row, $col, $rows, $cols );
        }
    }
    return $result;
}

sub count_word_occurrences {
    my ( $grid, $start_row, $start_col, $rows, $cols ) = @_;
    my $count = 0;

    foreach my $direction (@DIRECTIONS) {
        my ( $dx, $dy ) = @{$direction};
        $count +=
          check_direction( $grid, $start_row, $start_col, $dx, $dy, $rows,
            $cols );
    }

    return $count;
}

sub check_direction {
    my ( $grid, $x, $y, $dx, $dy, $rows, $cols ) = @_;

    for my $k ( 0 .. 3 ) {
        if (   $x < 0
            || $x >= $rows
            || $y < 0
            || $y >= $cols
            || $grid->[$x][$y] ne $XMAS[$k] )
        {
            return 0;
        }
        $x += $dx;
        $y += $dy;
    }
    return 1;
}

1;
