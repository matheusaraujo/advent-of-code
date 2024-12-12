use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my @map          = map { [ split //sm ] } @puzzle_input;
    my %visited      = ();
    my $total_price  = 0;

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[$i] } ) {
            if ( !( exists $visited{"$i,$j"} ) ) {
                my ( $area, undef, $corners ) =
                  solve( $i, $j, $map[$i][$j], \%visited, \@map );
                $total_price += $area * $corners;
            }
        }
    }

    return $total_price;
}

1;

# 835438
# 835438 too low
