use strict;
use warnings;

use List::Util qw/sum/;

sub part2 {
    my @puzzle_input = @_;
    @puzzle_input = map { split } $puzzle_input[0];

    return blinks( \@puzzle_input, 75 );
}

sub blinks {
    my ( $initial_stones, $blinks ) = @_;
    my %stones = ();
    for my $stone ( @{$initial_stones} ) {
        $stones{$stone}++;
    }

    foreach ( 1 .. $blinks ) {
        my %new_stones = ();
        for my $stone ( keys %stones ) {
            for my $t ( @{ transform_stone($stone) } ) {
                $new_stones{$t} += $stones{$stone};
            }
        }
        %stones = %new_stones;
    }

    return sum( values %stones );
}

1;
