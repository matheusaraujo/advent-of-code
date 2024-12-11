use strict;
use warnings;

sub parse_input {
    my @puzzle_input = @_;

    my @map = map { [ split //sm ] } @puzzle_input;
    my ( $m, $n ) = ( $#map, $#{ $map[0] } );
    my %antennas = ();

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            my $freq = $map[$i][$j];
            if ( !( $freq eq q{.} ) ) {
                if ( !exists $antennas{$freq} ) {
                    $antennas{$freq} = ();
                }
                push @{ $antennas{$freq} }, [ $i, $j ];
            }
        }
    }

    return ( $m, $n, \%antennas );
}

sub valid_point {
    my ( $x, $y, $m, $n ) = @_;
    return $x >= 0 && $x <= $m && $y >= 0 && $y <= $n;
}

1;
