use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    @puzzle_input = map { split } $puzzle_input[0];
    return blinks( \@puzzle_input, 25 );
}

sub blinks {
    my ( $initial_stones, $blinks ) = @_;
    my @stones = @{$initial_stones};

    foreach ( 1 .. $blinks ) {
        my @new_stones;
        for my $stone (@stones) {
            push @new_stones, @{ transform_stone($stone) };
        }
        @stones = @new_stones;
    }

    return scalar @stones;
}

1;
