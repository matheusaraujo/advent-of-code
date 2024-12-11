use strict;
use warnings;

sub get_initial_position {
    my @puzzle_input = @_;

    my @map = map { [ split //sm ] } @puzzle_input;
    my ( $x, $y, $m, $n ) = ( -1, -1, $#map, $#{ $map[0] } );

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            if ( $map[$i][$j] eq q{^} ) {
                $x = $i;
                $y = $j;
                last;
            }
        }
        if ( $x != -1 && $y != -1 ) {
            last;
        }
    }

    return ( $x, $y, @map );
}

sub walk_through_the_map {
    my ( $x, $y, $map_ref ) = @_;
    my ( $m, $n ) = ( $#{$map_ref}, $#{ $map_ref->[0] } );
    my @directions = ( [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] );
    my $dir        = 0;
    my %visited    = ();

    while (1) {
        if ( !exists $visited{"$x,$y"} ) {
            $visited{"$x,$y"} = [ $x, $y ];
        }

        my $next_x = $x + $directions[$dir][0];
        my $next_y = $y + $directions[$dir][1];

        if ( $next_x < 0 || $next_x > $m || $next_y < 0 || $next_y > $n ) {
            last;
        }
        elsif ( !( $map_ref->[$next_x][$next_y] eq q{#} ) ) {
            $x = $next_x;
            $y = $next_y;
        }
        else {
            $dir = ( $dir + 1 ) % scalar @directions;
        }
    }

    return values %visited;
}

sub look_for_loop {
    my ( $x0, $y0, $x1, $y1, $map_ref ) = @_;

    my @directions = ( [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] );
    my ( $m, $n ) = ( $#{$map_ref}, $#{ $map_ref->[0] } );
    my ( $x, $y, $direction ) = ( $x0, $y0, 0 );
    my %visited = ();

    while (1) {
        my $state = "$x,$y,$direction";
        if ( exists $visited{$state} ) {
            return 1;
        }
        $visited{$state} = 1;

        my $next_x = $x + $directions[$direction][0];
        my $next_y = $y + $directions[$direction][1];

        if ( $next_x < 0 || $next_x > $m || $next_y < 0 || $next_y > $n ) {
            return 0;
        }

        if (   !( $map_ref->[$next_x][$next_y] eq q{#} )
            && !( $next_x == $x1 && $next_y == $y1 ) )
        {
            $x = $next_x;
            $y = $next_y;
        }
        else {
            $direction = ( $direction + 1 ) % scalar @directions;
        }
    }

    return 0;
}

1;
