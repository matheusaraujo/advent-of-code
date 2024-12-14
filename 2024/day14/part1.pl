use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;

    my ( $x, $y, $mx, $my, $seconds ) = ( 101, 103, 50, 51, 100 );
    my ( $q1, $q2, $q3, $q4 ) = ( 0, 0, 0, 0 );

    for my $line (@puzzle_input) {
        my ( $px0, $py0, $vx, $vy ) =
          $line =~ /p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)/sxm;

        my $px = ( $px0 + $vx * $seconds ) % $x;
        my $py = ( $py0 + $vy * $seconds ) % $y;

        $q1 += $px < $mx && $py < $my ? 1 : 0;
        $q2 += $px > $mx && $py < $my ? 1 : 0;
        $q3 += $px < $mx && $py > $my ? 1 : 0;
        $q4 += $px > $mx && $py > $my ? 1 : 0;
    }

    return $q1 * $q2 * $q3 * $q4;
}

1;
