use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my ( $patterns, $designs ) = parse_input(@puzzle_input);
    return count_total_arrangements( $patterns, $designs );
}

sub count_total_arrangements {
    my ( $patterns, $designs ) = @_;
    my $count = 0;

    for my $design ( @{$designs} ) {
        $count += count_ways( $design, $patterns );
    }

    return $count;
}

sub count_ways {
    my ( $design, $patterns ) = @_;

    my @dp = (0) x ( length($design) + 1 );
    $dp[0] = 1;

    for my $i ( 1 .. length $design ) {
        for my $j ( 0 .. $i - 1 ) {
            my $substring = substr $design, $j, $i - $j;
            if ( $dp[$j] && exists $patterns->{$substring} ) {
                $dp[$i] += $dp[$j];
            }
        }
    }

    return $dp[ length $design ];
}

1;
