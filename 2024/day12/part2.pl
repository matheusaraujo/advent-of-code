use strict;
use warnings;

sub count_sides {
    my ( $h, $w, $grid ) = @_;
    my $sides = 0;

    for my $i ( 1 .. $h - 1 ) {
        for my $j ( 1 .. $w - 1 ) {
            my $bl = 0;

            $bl++ if $grid->[ $i - 1 ][ $j - 1 ] eq '#';
            $bl++ if $grid->[ $i - 1 ][$j] eq '#';
            $bl++ if $grid->[$i][ $j - 1 ] eq '#';
            $bl++ if $grid->[$i][$j] eq '#';

            if ( $bl == 1 || $bl == 3 ) {
                $sides++;
            }
        }
    }

    return $sides;
}

sub visit_part2 {
    my ( $i, $j, $plant_type, $visited_ref, $map_ref ) = @_;

    my ( $m, $n ) = ( $#{$map_ref}, $#{ $map_ref->[0] } );
    my @queue  = ( [ $i, $j ] );
    my $area   = 0;
    my $sides  = 0;
    my %points = ();

    while ( scalar @queue ) {
        my $current = shift @queue;
        my ( $x, $y ) = @{$current};
        $area++;

        $visited_ref->{"$x,$y"} = 1;
        $points{"$x,$y"} = 1;

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
                    $points{"$new_x,$new_y"} = 1;
                }
            }
        }

    }

    my @grid = ();
    for my $i ( 0 .. $n + 2 ) {
        $grid[0][$i] = ".";
    }
    for my $i ( 0 .. $m ) {
        $grid[ $i + 1 ][0] = ".";
        for my $j ( 0 .. $n ) {
            $grid[ $i + 1 ][ $j + 1 ] = exists $points{"$i,$j"} ? "#" : ".";
        }
        $grid[ $i + 1 ][ $n + 2 ] = ".";
    }
    for my $i ( 0 .. $n + 2 ) {
        $grid[ $m + 2 ][$i] = ".";
    }

    $sides = count_sides( $m + 3, $n + 3, \@grid );

    return ( $area, $sides );
}

sub part2 {
    my @puzzle_input = @_;
    my @map          = map { [ split //sm ] } @puzzle_input;
    my $total_price  = 0;
    my %visited      = ();

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[0] } ) {
            if ( !( exists $visited{"$i,$j"} ) ) {
                my ( $area, $sides ) =
                  visit_part2( $i, $j, $map[$i][$j], \%visited, \@map );
                $total_price += $area * $sides;

                print "$map[$i][$j] Area: $area, Sides: $sides\n";
            }
        }
    }

    return $total_price;
}

1;

# 835438 too low
