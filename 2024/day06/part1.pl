#!/usr/bin/perl
use strict;
use warnings;

sub part1 {
    my @puzzle_input  = @_;
    my $result        = 0;
    my $x             = -1;
    my $y             = -1;
    my $m             = -1;
    my $n             = -1;
    my @directions    = ( [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] );
    my @guard_symbols = qw{^ > v <};
    my $curr_dir      = 0;
    my @map;
    my %visited;

    chomp @puzzle_input;
    @map = map { [ split //sm ] } @puzzle_input;

    $m = $#map;
    $n = $#{ $map[0] };

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            for my $k ( 0 .. $#guard_symbols ) {
                if ( $map[$i][$j] eq $guard_symbols[$k] ) {
                    $x        = $i;
                    $y        = $j;
                    $curr_dir = $k;
                    last;
                }
            }
        }
        if ( $x != -1 && $y != -1 ) {
            last;
        }
    }

    $map[$x][$y] = q{.};

    while (1) {
        $visited{"$x,$y"} = 1;
        my $next_x = $x + $directions[$curr_dir][0];
        my $next_y = $y + $directions[$curr_dir][1];

        if ( $next_x < 0 || $next_x > $m || $next_y < 0 || $next_y > $n ) {
            last;
        }
        elsif ( $map[$next_x][$next_y] eq q{.} ) {
            $x = $next_x;
            $y = $next_y;
        }
        else {
            $curr_dir = ( $curr_dir + 1 ) % scalar @directions;
        }

    }

    return scalar keys %visited;
}

1;
