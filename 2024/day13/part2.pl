use strict;
use warnings;
use Readonly;

Readonly my $PART2_ADD => 1e13;

sub part2 {
    my @puzzle_input = @_;
    return solve( $PART2_ADD, @puzzle_input );
}

1;
