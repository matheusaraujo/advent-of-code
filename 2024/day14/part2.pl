use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;

    my ( $x, $y, $seconds ) = ( 101, 103, 0 );
    my @robots = ();

    for my $line (@puzzle_input) {
        my ( $px0, $py0, $vx, $vy ) =
          $line =~ /p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)/sxm;

        push @robots, { x => $px0, y => $py0, vx => $vx, vy => $vy };
    }

    while (1) {
        my %positions = ();
        for my $robot (@robots) {
            my $px = ( $robot->{x} + $robot->{vx} * $seconds ) % $x;
            my $py = ( $robot->{y} + $robot->{vy} * $seconds ) % $y;

            $positions{"$px,$py"} = 1;
        }
        if ( scalar keys %positions == scalar @robots ) {
            last;
        }
        $seconds++;
    }

    return $seconds;
}

1;
