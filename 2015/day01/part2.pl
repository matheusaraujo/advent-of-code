use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $floor        = 0;

    for my $i ( 1 .. length $puzzle_input[0] ) {
        my $char = substr $puzzle_input[0], $i - 1, 1;

        if ( $char eq '(' ) {
            $floor += 1;
        }
        elsif ( $char eq ')' ) {
            $floor -= 1;
        }

        if ( $floor == -1 ) {
            return $i;
        }
    }
    return 0;
}

1;
