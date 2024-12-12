use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my @map          = map { [ split //sm ] } @puzzle_input;
    my %visited      = ();
    my $total_price  = 0;

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[$i] } ) {
            if ( !( exists $visited{"$i,$j"} ) ) {
                my ( $area, $perimeter ) =
                  get_area_and_perimeter( $i, $j, $map[$i][$j], \%visited,
                    \@map );
                $total_price += $area * $perimeter;
            }
        }
    }

    return $total_price;
}

sub get_area_and_perimeter {
    my ( $i, $j, $plant_type, $visited_ref, $map_ref ) = @_;
    my ( $area, $perimeter ) = ( 0, 0 );
    my @queue = ( [ $i, $j ] );

    while (@queue) {
        my $current = shift @queue;
        my ( $x, $y ) = @{$current};

        next if $visited_ref->{"$x,$y"};
        $visited_ref->{"$x,$y"} = 1;
        $area++;

        for my $dir ( [ -1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ] ) {
            my ( $dx, $dy ) = @{$dir};
            my $new_x = $x + $dx;
            my $new_y = $y + $dy;

            if (   $new_x >= 0
                && $new_x <= $#{$map_ref}
                && $new_y >= 0
                && $new_y <= $#{ $map_ref->[0] } )
            {
                if ( $map_ref->[$new_x][$new_y] eq $plant_type ) {
                    if ( !exists $visited_ref->{"$new_x,$new_y"} ) {
                        push @queue, [ $new_x, $new_y ];
                    }
                }
                else {
                    $perimeter++;
                }
            }
            else {
                $perimeter++;
            }
        }
    }
    return $area, $perimeter;
}

1;
