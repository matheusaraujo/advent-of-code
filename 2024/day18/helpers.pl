use strict;
use warnings;

sub dfs {

    my ( $size, $corrupted ) = @_;
    my @directions = ( [ 0, 1 ], [ 1, 0 ], [ 0, -1 ], [ -1, 0 ] );
    my @queue      = ( [ 0, 0, 0 ] );
    my %visited    = ();
    $visited{'0,0'} = 1;

    while (@queue) {

        my $current = shift @queue;
        my ( $x, $y, $steps ) = @{$current};

        if ( $x == $size - 1 && $y == $size - 1 ) {
            return $steps;
        }

        for my $direction (@directions) {
            my ( $dx, $dy ) = @{$direction};

            my $nx = $x + $dx;
            my $ny = $y + $dy;

            if (   $nx < 0
                || $nx >= $size
                || $ny < 0
                || $ny >= $size
                || exists $visited{"$nx,$ny"}
                || exists $corrupted->{"$nx,$ny"} )
            {
                next;
            }

            $visited{"$nx,$ny"} = 1;
            push @queue, [ $nx, $ny, $steps + 1 ];
        }
    }

    return -1;
}

1;
