use strict;
use warnings;

sub part2 {
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

    for my $move (@moves) {
        my ( $dx, $dy ) = @{ $dirs{$move} };
        my ( $nx, $ny ) = ( $x + $dx, $y + $dy );

        if    ( $map[$nx][$ny] eq q{#} ) { }
        elsif ( $map[$nx][$ny] eq q{.} ) {
            $x = $nx;
            $y = $ny;
        }
        elsif ( $map[$nx][$ny] eq q{[} || $map[$nx][$ny] eq ']' ) {
            if ( $move eq q{<} || $move eq q{>} ) {
                while ( $map[$nx][$ny] eq q{[} || $map[$nx][$ny] eq ']' ) {
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
            elsif ( is_possible_to_move( $x, $y, $dx, $dy, \@map ) ) {
                move( $x + $dx, $y + $dy, $dx, $dy, \@map );
                ( $x, $y ) = ( $x + $dx, $y + $dy );
            }
        }
    }

    for my $i ( 0 .. $#map ) {
        for my $j ( 0 .. $#{ $map[$i] } ) {
            if ( $map[$i][$j] eq q{[} ) {
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
    my ( $x, $y, $x0, $y0 ) = ( 0, 0, 0, 0 );

    for my $line (@puzzle_input) {
        if ( length $line == 0 ) {
            last;
        }

        my @row        = split //smx, $line;
        my @parsed_row = ();

        $y = 0;
        for my $cell (@row) {
            if ( $cell eq q{#} || $cell eq q{.} ) {
                push @parsed_row, $cell;
                push @parsed_row, $cell;
            }
            elsif ( $cell eq q{O} ) {
                push @parsed_row, q{[};
                push @parsed_row, ']';
            }
            elsif ( $cell eq q{@} ) {
                push @parsed_row, q{.};
                push @parsed_row, q{.};
                $x0 = $x;
                $y0 = $y;
            }
            $y += 2;
        }
        push @map, \@parsed_row;
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

sub is_possible_to_move {
    my ( $x, $y, $dx, $dy, $map_ref ) = @_;

    if ( $map_ref->[ $x + $dx ][ $y + $dy ] eq q{#} ) {
        return 0;
    }
    if ( $map_ref->[ $x + $dx ][ $y + $dy ] eq q{.} ) {
        return 1;
    }

    if ( $map_ref->[ $x + $dx ][ $y + $dy ] eq q{[} ) {
        return is_possible_to_move( $x + $dx, $y + $dy, $dx, $dy, $map_ref )
          && is_possible_to_move( $x + $dx, $y + $dy + 1, $dx, $dy, $map_ref );
    }
    elsif ( $map_ref->[ $x + $dx ][ $y + $dy ] eq q{]} ) {
        return is_possible_to_move( $x + $dx, $y + $dy, $dx, $dy, $map_ref )
          && is_possible_to_move( $x + $dx, $y + $dy - 1, $dx, $dy, $map_ref );
    }
}

sub move {
    my ( $x, $y, $dx, $dy, $map_ref ) = @_;
    $y = $map_ref->[$x][$y] eq q{[} ? $y : $y - 1;

    if ( $map_ref->[ $x + $dx ][ $y + $dy ] ne q{.} ) {
        move( $x + $dx, $y + $dy, $dx, $dy, $map_ref );
    }
    if ( $map_ref->[ $x + $dx ][ $y + $dy + 1 ] ne q{.} ) {
        move( $x + $dx, $y + $dy + 1, $dx, $dy, $map_ref );
    }

    $map_ref->[ $x + $dx ][ $y + $dy ]     = $map_ref->[$x][$y];
    $map_ref->[ $x + $dx ][ $y + 1 + $dy ] = $map_ref->[$x][ $y + 1 ];
    $map_ref->[$x][$y]                     = q{.};
    $map_ref->[$x][ $y + 1 ]               = q{.};
    return;
}

1;
