use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;

    my $result = 0;
    my ( $start, $end, $tiles ) = parse_input(@puzzle_input);
    my $visited   = dijkstra( $start, $tiles );
    my $min_score = get_min_score( $visited, $end );

    my $target = q{};

    for my $key ( keys %{$visited} ) {
        my ( $x, $y, $dir ) = split /,/sxm, $key;
        if (   $x == $end->[0]
            && $y == $end->[1]
            && $visited->{$key} == $min_score )
        {
            $target = $key;
            last;
        }
    }

    my $seen = backtrack( $visited, $target );
    return scalar keys %{$seen};
}

sub backtrack {
    my ( $visited, $end ) = @_;
    my @dirs  = ( [ 1, 0 ], [ 0, 1 ], [ -1, 0 ], [ 0, -1 ] );
    my %seen  = ();
    my @queue = ();

    push @queue, ($end);

    while (@queue) {
        my $key = shift @queue;

        my ( $x, $y, $dir ) = split /,/sxm, $key;
        $seen{"$x,$y"} = 1;

        my ( $nx, $ny ) = ( $x - $dirs[$dir][0], $y - $dirs[$dir][1] );
        my $nkey = "$nx,$ny,$dir";

        if ( exists $visited->{$nkey}
            && $visited->{$nkey} + 1 == $visited->{"$key"} )
        {
            push @queue, ($nkey);
        }

        for my $delta ( 1, -1 ) {
            my $ndir = ( $dir + $delta ) % 4;
            $nkey = "$x,$y,$ndir";

            if ( exists $visited->{$nkey}
                && $visited->{$nkey} + 1000 == $visited->{"$key"} )
            {
                push @queue, ($nkey);
            }
        }
    }

    return \%seen;
}

1;

