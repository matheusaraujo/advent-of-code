use strict;
use warnings;

sub part1 {
    my @puzzle_input = @_;
    my ( $map_ref, $moves_ref, $x, $y ) = parse_input(@puzzle_input);
    my @map    = @{$map_ref};
    my @moves  = @{$moves_ref};
    my $result = 0;

    my %dirs = (
        q{^} => [ -1, 0 ],
        q{v} => [ 1,  0 ],
        q{<} => [ 0,  -1 ],
        q{>} => [ 0,  1 ],
    );

    $map[$x][$y] = q{.};

    for my $move (@moves) {
        my ( $dx, $dy ) = @{ $dirs{$move} };
        my ( $nx, $ny ) = ( $x + $dx, $y + $dy );

        if    ( $map[$nx][$ny] eq q{#} ) { }
        elsif ( $map[$nx][$ny] eq q{.} ) {
            $x = $nx;
            $y = $ny;
        }
        elsif ( $map[$nx][$ny] eq q{O} ) {
            while ( $map[$nx][$ny] eq q{O} ) {
                ( $nx, $ny ) = ( $nx + $dx, $ny + $dy );
            }
            if ( $map[$nx][$ny] eq q{#} ) { }
            else {
                while ( !( $nx == $x && $ny == $y ) ) {
                    $map[$nx][$ny] = $map[ $nx - $dx ][ $ny - $dy ];
                    ( $nx, $ny ) = ( $nx - $dx, $ny - $dy );
                }
                ( $x, $y ) = ( $x + $dx, $y + $dy );
            }
        }
    }

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[$i] } ) {
            if ( $map[$i][$j] eq q{O} ) {
                $result += $i * 100 + $j;
            }
        }
    }

    return $result;
}

sub parse_input {
    my @puzzle_input = @_;
    my @map          = ();
    my @moves        = ();
    my ( $x, $x0, $y0 ) = ( 0, 0, 0 );

    for my $line (@puzzle_input) {
        if ( length $line == 0 ) {
            last;
        }
        if ( index( $line, q{@} ) != -1 ) {
            ( $x0, $y0 ) = ( $x, index $line, q{@} );
        }
        my @row = split //smx, $line;
        push @map, \@row;
        $x++;
    }

    for my $i ( $x + 1 .. $#puzzle_input ) {
        my @row = split //smx, $puzzle_input[$i];
        for my $move (@row) {
            push @moves, $move;
        }
    }

    return ( \@map, \@moves, $x0, $y0 );
}

1;
