use strict;
use warnings;

use List::Util qw/sum/;

sub part2 {
    my @puzzle_input = @_;
    my ( $x0, $y0, @map ) = get_initial_position(@puzzle_input);
    my @visited = walk_through_the_map( $x0, $y0, \@map );

    return sum map { look_for_loop( $x0, $y0, @{$_}[0], @{$_}[1], \@map ) }
      @visited;
}

1;
