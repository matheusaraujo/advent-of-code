use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $m, $n, $antennas_ref ) = parse_input(@puzzle_input);
    my %antennas  = %{$antennas_ref};
    my %antinodes = ();

    for my $freq ( keys %antennas ) {
        my @positions = @{ $antennas{$freq} };
        for my $i ( 0 .. $#positions ) {
            for my $j ( $i + 1 .. $#positions ) {
                my @p1 = @{ $positions[$i] };
                my @p2 = @{ $positions[$j] };

                for my $p (
                    [ 2 * $p1[0] - $p2[0], 2 * $p1[1] - $p2[1] ],
                    [ 2 * $p2[0] - $p1[0], 2 * $p2[1] - $p1[1] ]
                  )
                {
                    my ( $x, $y ) = @{$p};
                    if ( valid_point $x, $y, $m, $n ) {
                        $antinodes{"$x,$y"} = 1;
                    }
                }
            }
        }
    }

    return scalar %antinodes;
}

1;

