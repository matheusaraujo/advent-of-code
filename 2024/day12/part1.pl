use strict;
use warnings;

sub visit_part1 {
    my ( $i, $j, $plant_type, $visited_ref, $map_ref ) = @_;

    my ( $m, $n ) = ( $#{$map_ref}, $#{ $map_ref->[0] } );
    my ( $area, $perimeter ) = ( 0, 0 );
    my @queue = ( [ $i, $j ] );

    while ( scalar @queue ) {
        my $current = shift @queue;
        my ( $x, $y ) = @{$current};
        $area++;

        $visited_ref->{"$x,$y"} = 1;

        for my $dir ( [ -1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ] ) {
            my ( $dx, $dy ) = @{$dir};
            my $new_x = $x + $dx;
            my $new_y = $y + $dy;

            if ( $new_x >= 0 && $new_x <= $m && $new_y >= 0 && $new_y <= $n ) {
                if ( $map_ref->[$new_x][$new_y] eq $plant_type
                    && !( exists $visited_ref->{"$new_x,$new_y"} ) )
                {
                    $visited_ref->{"$new_x,$new_y"} = 1;
                    push @queue, [ $new_x, $new_y ];
                }
                elsif ( $map_ref->[$new_x][$new_y] ne $plant_type ) {
                    $perimeter++;
                }
            }
            else {
                $perimeter++;
            }
        }
    }

    return ( $area, $perimeter );
}

sub part1 {
    my @puzzle_input = @_;
    my @map          = map { [ split //sm ] } @puzzle_input;
    my $total_price  = 0;
    my %visited      = ();

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[0] } ) {
            if ( !( exists $visited{"$i,$j"} ) ) {
                my ( $area, $perimeter ) =
                  visit_part1( $i, $j, $map[$i][$j], \%visited, \@map );
                $total_price += $area * $perimeter;
            }
        }
    }

    return $total_price;
}

1;
