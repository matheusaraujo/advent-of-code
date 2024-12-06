#!/usr/bin/perl
use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my ( $x, $y, $curr_dir )                    = ( -1, -1, -1 );
    my ( $initial_x, $initial_y, $initial_dir ) = ( -1, -1, -1 );
    my ( $m, $n, $loop_count )                  = ( -1, -1, 0 );
    my @directions    = ( [ -1, 0 ], [ 0, 1 ], [ 1, 0 ], [ 0, -1 ] );
    my @guard_symbols = qw{^ > v <};
    my @map;
    my @candidate_points;

    chomp @puzzle_input;
    @map = map { [ split //sm ] } @puzzle_input;

    $m = $#map;
    $n = $#{ $map[0] };

    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            for my $k ( 0 .. $#guard_symbols ) {
                if ( $map[$i][$j] eq $guard_symbols[$k] ) {
                    $initial_x   = $i;
                    $initial_y   = $j;
                    $initial_dir = $k;
                    last;
                }
            }
        }
        if ( $initial_x != -1 && $initial_y != -1 ) {
            last;
        }
    }

    # instead of include all positions in the candidate_points array,
    # we could just include neighbor positions to the regular path
    for my $i ( 0 .. $m ) {
        for my $j ( 0 .. $n ) {
            if ( $map[$i][$j] eq q{.} ) {
                push @candidate_points, [ $i, $j ];
            }
        }
    }

    $map[$initial_x][$initial_y] = q{.};

    foreach my $point (@candidate_points) {
        my ( $test_x, $test_y ) = @{$point};

        $map[$test_x][$test_y] = q{#};
        my %visited = ();
        $x        = $initial_x;
        $y        = $initial_y;
        $curr_dir = $initial_dir;
        my $is_loop = 0;

        while (1) {
            my $state = "$x,$y,$curr_dir";
            if ( $visited{$state}++ ) {
                $is_loop = 1;
                last;
            }

            my $next_x = $x + $directions[$curr_dir][0];
            my $next_y = $y + $directions[$curr_dir][1];

            if (   $next_x < 0
                || $next_x > $m
                || $next_y < 0
                || $next_y > $n )
            {
                $is_loop = 0;
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

        $loop_count += $is_loop;
        $map[$test_x][$test_y] = q{.};
    }

    return $loop_count;
}

1;
