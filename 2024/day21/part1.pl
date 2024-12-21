## no critic (CodeLayout::ProhibitParensWithBuiltins)

use strict;
use warnings;

require helpers;

sub part1 {
    my @puzzle_input = @_;
    my $complexity   = 0;

    for my $code (@puzzle_input) {
        my $num_route  = move_numeric_keypad($code);
        my $rad_route  = move_directional_keypad($num_route);
        my $cold_route = move_directional_keypad($rad_route);
        $complexity += length($cold_route) * substr( $code, 0, -1 );
    }

    return $complexity;
}

1;
