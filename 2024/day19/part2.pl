use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my ( $patterns, $designs ) = parse_input(@puzzle_input);
    return count_total_arrangements( $patterns, $designs );
}

sub count_total_arrangements {
    my ( $patterns, $designs ) = @_;
    my $count = 0;

    for my $design ( @{$designs} ) {
        $count += count_ways( $design, $patterns );
    }

    return $count;
}

1;
