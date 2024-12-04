#!/usr/bin/perl
use strict;
use warnings;

use Readonly;

Readonly my $PAIR1 => 'MS';
Readonly my $PAIR2 => 'SM';

sub part2 {
    my @puzzle_input = @_;
    my @word_search  = parse_input(@puzzle_input);
    my ( $rows, $cols ) = ( scalar @word_search, scalar @{ $word_search[0] } );
    my $result = 0;

    for my $row ( 0 .. $rows - 1 ) {
        for my $col ( 0 .. $cols - 1 ) {
            if ( $word_search[$row][$col] eq 'A' ) {
                $result += count_diagonal_matches( \@word_search,
                    $row, $col, $rows, $cols );
            }
        }
    }

    return $result;
}

sub count_diagonal_matches {
    my ( $grid, $row, $col, $rows, $cols ) = @_;

    my $left_up    = get_cell( $grid, $row - 1, $col - 1, $rows, $cols );
    my $right_up   = get_cell( $grid, $row - 1, $col + 1, $rows, $cols );
    my $left_down  = get_cell( $grid, $row + 1, $col - 1, $rows, $cols );
    my $right_down = get_cell( $grid, $row + 1, $col + 1, $rows, $cols );

    my $diagonal1 = $left_up . $right_down;
    my $diagonal2 = $right_up . $left_down;

    return ( is_valid_pair($diagonal1) && is_valid_pair($diagonal2) ) ? 1 : 0;
}

sub get_cell {
    my ( $grid, $row, $col, $rows, $cols ) = @_;
    return
         $row < 0
      || $row >= $rows
      || $col < 0
      || $col >= $cols ? q{} : $grid->[$row][$col];
}

sub is_valid_pair {
    my ($diagonal) = @_;
    return $diagonal eq $PAIR1 || $diagonal eq $PAIR2;
}

1;
