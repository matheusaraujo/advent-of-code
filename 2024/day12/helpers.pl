use strict;
use warnings;

sub solve {
    my ( $i, $j, $plant_type, $visited_ref, $map_ref ) = @_;

    my ( $area, $perimeter ) = ( 0, 0 );

    my %corners = ();
    my @queue   = ( [ $i, $j ] );

    while (@queue) {
        my $current = shift @queue;
        my ( $x, $y ) = @{$current};

        next if $visited_ref->{"$x,$y"};

        $visited_ref->{"$x,$y"} = 1;
        $area++;

        push @{ $corners{"$x,$y"} }, [ $x, $y ];
        push @{ $corners{ "$x," . ( $y + 1 ) } }, [ $x, $y ];
        push @{ $corners{ ( $x + 1 ) . ",$y" } }, [ $x, $y ];
        push @{ $corners{ ( $x + 1 ) . q{,} . ( $y + 1 ) } }, [ $x, $y ];

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

    my $unique_corners = 0;
    foreach my $corner ( keys %corners ) {
        my $c = scalar @{ $corners{$corner} };
        if ( $c == 1 || $c == 3 ) {
            $unique_corners++;
        }
        elsif (
            $c == 2
            && (   $corners{$corner}[0][0] != $corners{$corner}[1][0]
                && $corners{$corner}[0][1] != $corners{$corner}[1][1] )
          )
        {
            $unique_corners += 2;
        }
    }

    return $area, $perimeter, $unique_corners;

}

1;

