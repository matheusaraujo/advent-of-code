use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $x, $y, @map ) = get_initial_position(@puzzle_input);
    return scalar walk_through_the_map( $x, $y, \@map );
}

1;
