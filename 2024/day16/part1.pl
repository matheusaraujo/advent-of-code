use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my $result       = 'inf';
    my ( $start, $end, $tiles ) = parse_input(@puzzle_input);
    my $visited = dijkstra( $start, $tiles );
    return get_min_score( $visited, $end );
}

1;
