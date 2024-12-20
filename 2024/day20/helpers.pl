## no critic (RegularExpressions::RequireDotMatchAnything)
## no critic (RegularExpressions::RequireLineBoundaryMatching)
## no critic (RegularExpressions::RequireExtendedFormatting)
## no critic (ValuesAndExpressions::ProhibitNoisyQuotes)
## no critic (CodeLayout::ProhibitParensWithBuiltins)

# TODO: @matheusaraujo, this code really needs to be refactored
# it's brute force solution, it's taking around 40s to run each part
# also need to remove all those no critic lines

use strict;
use warnings;

sub solve {
    my ( $limit, @puzzle_input ) = @_;
    my @map = ();
    my $end = q{};

    for my $line (@puzzle_input) {
        my @row = split //, $line;
        push @map, \@row;
    }

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[0] } ) {
            if ( $map[$i][$j] eq 'E' ) {
                $end = "$i,$j";
                $map[$i][$j] = '.';
            }
        }
    }

    my $distances = dfs( \@map, $end );
    my $cheats    = 0;

    for my $position1 ( keys %{$distances} ) {
        for my $position2 ( keys %{$distances} ) {
            if ( $position1 eq $position2 ) {
                next;
            }

            my ( $x1, $y1 ) = split /,/, $position1;
            my ( $x2, $y2 ) = split /,/, $position2;
            my $distance = abs( $x1 - $x2 ) + abs( $y1 - $y2 );
            if (
                $distance <= $limit
                && ( $distances->{$position1} -
                    $distances->{$position2} -
                    $distance ) >= 100
              )
            {
                $cheats++;
            }
        }
    }

    return $cheats;
}

sub dfs {
    my ( $map, $start ) = @_;

    my @queue     = ();
    my %distances = ();

    push @queue, $start;
    $distances{$start} = 0;

    while (@queue) {
        my $current = shift @queue;
        my ( $x, $y ) = split /,/, $current;

        for my $direction ( [ 0, 1 ], [ 0, -1 ], [ 1, 0 ], [ -1, 0 ] ) {
            my ( $dx, $dy ) = @{$direction};
            my $new_x = $x + $dx;
            my $new_y = $y + $dy;
            my $new   = "$new_x,$new_y";

            if (
                   $new_x < 0
                || $new_x >= scalar @{$map}
                || $new_y < 0
                || $new_y >= scalar @{ $map->[0] }
                || $map->[$new_x][$new_y] eq '#'
                || ( exists $distances{"$new"}
                    && $distances{"$new"} < $distances{$current} + 1 )
              )
            {
                next;
            }

            $distances{"$new"} = $distances{$current} + 1;
            push @queue, "$new";
        }
    }

    return \%distances;
}

1;
