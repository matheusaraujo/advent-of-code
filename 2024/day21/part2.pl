## no critic (CodeLayout::ProhibitParensWithBuiltins)
## no critic (ControlStructures::ProhibitPostfixControls])

use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $complexity   = 0;

    my @numeric_routes = map { move_numeric_keypad($_) } @puzzle_input;

    my @robot_routes = map {
        { $_ => 1 }
    } @numeric_routes;

    for ( 1 .. 25 ) {
        my @new_routes;
        for my $route_counter (@robot_routes) {
            my %new_route;
            for my $sub_route ( keys %{$route_counter} ) {
                my $new_counts = move_part2($sub_route);
                $new_route{$_} +=
                  ( $new_counts->{$_} * $route_counter->{$sub_route} )
                  for keys %{$new_counts};
            }
            push @new_routes, \%new_route;
        }
        @robot_routes = @new_routes;
    }

    for my $i ( 0 .. $#puzzle_input ) {
        my $code  = $puzzle_input[$i];
        my $route = $robot_routes[$i];
        $complexity += route_length($route) * substr( $code, 0, -1 );
    }

    return $complexity;
}

1;

