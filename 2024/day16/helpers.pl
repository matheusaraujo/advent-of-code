use strict;
use warnings;

sub parse_input {
    my @puzzle_input = @_;
    my @start        = ( -1, -1 );
    my @end          = ( -1, -1 );
    my %tiles        = ();

    for my $j ( 0 .. $#puzzle_input ) {
        my @line = split //sxm, $puzzle_input[$j];
        for my $i ( 0 .. $#line ) {
            if ( $line[$i] eq 'S' ) {
                @start = ( $i, $j );
            }
            elsif ( $line[$i] eq 'E' ) {
                @end = ( $i, $j );
                $tiles{"$i,$j"} = 1;
            }
            elsif ( $line[$i] eq q{.} ) {
                $tiles{"$i,$j"} = 1;
            }
        }
    }

    return ( \@start, \@end, \%tiles );
}

sub dijkstra {
    my ( $start, $tiles ) = @_;

    my @dirs = ( [ 1, 0 ], [ 0, 1 ], [ -1, 0 ], [ 0, -1 ] );

    my %visited = ();
    my @queue   = ();

    # score, direction, position
    push @queue, ( [ 0, 0, $start ] );

    # position, direction
    $visited{"$start->[0],$start->[1],0"} = 0;

    while (@queue) {
        my ( $score, $dir, $pos ) = @{ shift @queue };
        my ( $x, $y ) = @{$pos};

        if ( exists $visited{"$x,$y,$dir"} && $visited{"$x,$y,$dir"} < $score )
        {
            next;
        }

        my ( $nx, $ny ) = ( $x + $dirs[$dir][0], $y + $dirs[$dir][1] );

        if ( exists $tiles->{"$nx,$ny"} ) {
            my $nkey = "$nx,$ny,$dir";
            if ( !exists $visited{$nkey} || $visited{$nkey} > $score + 1 ) {
                $visited{$nkey} = $score + 1;
                push @queue, ( [ $score + 1, $dir, [ $nx, $ny ] ] );
            }
        }

        for my $delta ( -1, 1 ) {
            my $ndir = ( $dir + $delta ) % 4;
            my $nkey = "$x,$y,$ndir";
            if ( !exists $visited{$nkey} || $visited{$nkey} > $score + 1000 ) {
                $visited{$nkey} = $score + 1000;
                push @queue, ( [ $score + 1000, $ndir, [ $x, $y ] ] );
            }
        }
    }

    return \%visited;
}

sub get_min_score {
    my ( $visited, $end ) = @_;
    my $result = 'inf';
    for my $key ( keys %{$visited} ) {
        my ( $x, $y, $dir ) = split /,/sxm, $key;
        if ( $x == $end->[0] && $y == $end->[1] && $visited->{$key} < $result )
        {
            $result = $visited->{$key};
        }
    }
    return $result;
}

1;
