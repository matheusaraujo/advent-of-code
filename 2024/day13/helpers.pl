## no critic (RegularExpressions::RequireExtendedFormatting)

use strict;
use warnings;

sub solve {
    my ( $add, @puzzle_input ) = @_;
    my $result = 0;

    foreach my $i ( grep { $_ % 4 == 0 } 0 .. $#puzzle_input ) {

        my ( $a1, $a2, $b1, $b2, $c1, $c2 ) =
          parse_input( \@puzzle_input, $i, $add );

        my $determinant = calc_determinant( $a1, $a2, $b1, $b2 );

        if ( $determinant != 0 ) {
            my $x = calc_x( $determinant, $b2, $c1, $b1, $c2 );
            my $y = calc_y( $determinant, $a1, $c2, $a2, $c1 );

            if ( $x =~ /^-?\d+$/smx && $y =~ /^-?\d+$/smx ) {
                $result += 3 * $x + $y;
            }
        }
    }
    return $result;
}

sub parse_input {
    my ( $input_ref, $line, $add ) = @_;

    my ( $a1, $a2 ) =
      @{$input_ref}[$line] =~ /Button A: X[+](\d+), Y[+](\d+)/sm;
    my ( $b1, $b2 ) =
      @{$input_ref}[ $line + 1 ] =~ /Button B: X[+](\d+), Y[+](\d+)/sm;
    my ( $c1, $c2 ) =
      @{$input_ref}[ $line + 2 ] =~ /Prize: X=(\d+), Y=(\d+)/sm;

    return ( $a1, $a2, $b1, $b2, $c1 + $add, $c2 + $add );
}

sub calc_determinant {
    my ( $a1, $a2, $b1, $b2 ) = @_;
    return $a1 * $b2 - $a2 * $b1;
}

sub calc_x {
    my ( $determinant, $b2, $c1, $b1, $c2 ) = @_;
    return 1 / $determinant * ( $b2 * $c1 - $b1 * $c2 );
}

sub calc_y {
    my ( $determinant, $a1, $c2, $a2, $c1 ) = @_;
    return 1 / $determinant * ( $a1 * $c2 - $a2 * $c1 );
}

1;
