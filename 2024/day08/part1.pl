#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    chomp @puzzle_input;

    my @map = map { [ split //sm ] } @puzzle_input;
    my ( $m, $n ) = ( $#map, $#{ $map[0] } );
    my $result    = 0;
    my %antennas  = ();
    my %antinodes = ();

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

    for my $freq ( keys %antennas ) {
        my @positions = @{ $antennas{$freq} };
        for my $i ( 0 .. $#positions ) {
            for my $j ( $i + 1 .. $#positions ) {
                my @p1 = @{ $positions[$i] };
                my @p2 = @{ $positions[$j] };

                my $x1 = 2 * $p1[0] - $p2[0];
                my $y1 = 2 * $p1[1] - $p2[1];

                if ( $x1 >= 0 && $x1 <= $m && $y1 >= 0 && $y1 <= $n ) {
                    $antinodes{"$x1,$y1"} = 1;
                }

                my $x2 = 2 * $p2[0] - $p1[0];
                my $y2 = 2 * $p2[1] - $p1[1];

                if ( $x2 >= 0 && $x2 <= $m && $y2 >= 0 && $y2 <= $n ) {
                    $antinodes{"$x2,$y2"} = 1;
                }
            }
        }
    }

    return scalar %antinodes;
}

1;

