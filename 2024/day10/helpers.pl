use strict;
use warnings;

sub valid_step {
    my ( $x, $y, $curr, $map_ref ) = @_;
    if ( $x < 0 || $x > $#{$map_ref} || $y < 0 || $y > $#{ $map_ref->[0] } ) {
        return 0;
    }
    return $map_ref->[$x][$y] == ( $curr + 1 );
}

sub hikes {
    my ( $i, $j, $rating, $map_ref ) = @_;

    my @queue   = ( [ $i, $j ] );
    my %visited = ();
    my $result  = 0;

    while (@queue) {
        my $current = shift @queue;
        my ( $x, $y ) = @{$current};

        if ( exists $visited{ ( $x, $y ) } && !$rating ) {
            next;
        }

        $visited{ ( $x, $y ) } = 1;
        if ( $map_ref->[$x][$y] == 9 ) {
            $result++;
            next;
        }

        for my $dir ( [ -1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ] ) {
            my ( $dx, $dy ) = @{$dir};
            my $new_x = $x + $dx;
            my $new_y = $y + $dy;

            if ( valid_step( $new_x, $new_y, $map_ref->[$x][$y], $map_ref ) ) {
                push @queue, [ $new_x, $new_y ];
            }
        }
    }

    return $result;
}

sub solve {
    my ( $rating, @puzzle_input ) = @_;
    my $result = 0;

    my @map = map { [ split //sm ] } @puzzle_input;
    my ( $m, $n ) = ( $#map, $#{ $map[0] } );

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            if ( $map[$i][$j] == 0 ) {
                $result += hikes( $i, $j, $rating, \@map );
            }
        }
    }

    return $result;
}

1;
