use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $patterns, $designs ) = parse_input(@puzzle_input);
    return count_possible_designs( $patterns, $designs );
}

sub count_possible_designs {
    my ( $patterns, $designs ) = @_;
    my $count = 0;

    for my $design ( @{$designs} ) {
        $count += is_possible_design( $design, $patterns ) ? 1 : 0;
    }

    return $count;
}

sub is_possible_design {
    my ( $design, $patterns ) = @_;

    my @dp = (0) x ( length($design) + 1 );
    $dp[0] = 1;

    for my $i ( 1 .. length $design ) {
        for my $j ( 0 .. $i - 1 ) {
            my $substring = substr $design, $j, $i - $j;
            if ( $dp[$j] && exists $patterns->{$substring} ) {
                $dp[$i] = 1;
                last;
            }
        }
    }

    return $dp[ length $design ];
}

1;
