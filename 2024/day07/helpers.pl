use strict;
use warnings;

sub backtrack {
    my ( $current_ref, $level, $length, $operators_ref, $result_ref ) = @_;

    if ( $level == $length ) {
        push @{$result_ref}, [ @{$current_ref} ];
        return;
    }

    foreach my $op ( @{$operators_ref} ) {
        push @{$current_ref}, $op;
        backtrack( $current_ref, $level + 1, $length, $operators_ref,
            $result_ref );
        pop @{$current_ref};
    }

    return;
}

sub generate_combinations {
    my ( $length, @operators ) = @_;
    my @result;
    my @current;
    backtrack( \@current, 0, $length, \@operators, \@result );
    return @result;
}

sub solve {
    my ( $puzzle_input_ref, $operators_ref ) = @_;
    my @operators          = @{$operators_ref};
    my @puzzle_input       = @{$puzzle_input_ref};
    my $result             = 0;
    my %combinations_cache = ();

    for my $equation (@puzzle_input) {
        my @parts   = split /:/sxm, $equation;
        my $target  = $parts[0];
        my @numbers = split q{ }, $parts[1];

        my @combinations = ();
        if ( exists $combinations_cache{$#numbers} ) {
            @combinations = @{ $combinations_cache{$#numbers} };
        }
        else {
            @combinations = generate_combinations( $#numbers, @operators );
            $combinations_cache{$#numbers} = \@combinations;
        }

        for my $combination (@combinations) {
            my $tmp = $numbers[0];

            for my $i ( 1 .. $#numbers ) {
                if ( $combination->[ $i - 1 ] eq q{+} ) {
                    $tmp += $numbers[$i];
                }
                elsif ( $combination->[ $i - 1 ] eq q{*} ) {
                    $tmp *= $numbers[$i];
                }
                elsif ( $combination->[ $i - 1 ] eq q{||} ) {
                    $tmp .= $numbers[$i];
                }

                if ( $tmp > $target ) {
                    last;
                }
            }

            if ( $tmp == $target ) {
                $result += $target;
                last;
            }

        }
    }

    return $result;
}

1;
