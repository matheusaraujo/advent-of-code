## no critic (Subroutines::ProhibitExcessComplexity)
## no critic (ControlStructures::ProhibitCascadingIfElse)
## no critic (RegularExpressions::RequireExtendedFormatting)

# TODO: @matheusaraujo - this code strongly needs refactoring
# TODO: @matheusaraujo - write this solution explanation, based on https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2gge90/

use strict;
use warnings;
use Readonly;

Readonly my $INSTRUCTION_ADV => 0;
Readonly my $INSTRUCTION_BXL => 1;
Readonly my $INSTRUCTION_BST => 2;
Readonly my $INSTRUCTION_JNZ => 3;
Readonly my $INSTRUCTION_BXC => 4;
Readonly my $INSTRUCTION_OUT => 5;
Readonly my $INSTRUCTION_BDV => 6;
Readonly my $INSTRUCTION_CDV => 7;

sub part2 {
    my @puzzle_input = @_;

    my $register_a  = 0;
    my $register_b  = int( $puzzle_input[1] =~ s/Register B: //smr );
    my $register_c  = int( $puzzle_input[2] =~ s/Register C: //smr );
    my @program     = split /,/smx, $puzzle_input[4] =~ s/Program: //smr;
    my $program_str = join q{,}, @program;
    my $output      = q{};

    return get_register_a_candidate( $#program, 0, @program );
}

sub get_register_a_candidate {
    my ( $cursor, $sofar, @program ) = @_;

    for my $candidate ( 0 .. 7 ) {
        my $output = simulate( $sofar * 8 + $candidate, 0, 0, @program );
        my $program_output = join q{,}, @program[ $cursor .. $#program ];

        if ( $output eq $program_output ) {
            if ( $cursor == 0 ) {
                return $sofar * 8 + $candidate;
            }
            my $ret = get_register_a_candidate( $cursor - 1,
                $sofar * 8 + $candidate, @program );
            if ( $ret != -1 ) {
                return $ret;
            }
        }
    }
    return -1;
}

sub simulate {

    my ( $register_a, $register_b, $register_c, @program ) = @_;
    my @out = ();

    my $instruction_pointer = 0;

    while ( $instruction_pointer < scalar @program ) {
        my $opcode = $program[$instruction_pointer];

        if (   $opcode == $INSTRUCTION_ADV
            || $opcode == $INSTRUCTION_BDV
            || $opcode == $INSTRUCTION_CDV )
        {
            my $operand = $program[ $instruction_pointer + 1 ];
            my $combo_operand =
                $operand == 4 ? $register_a
              : $operand == 5 ? $register_b
              : $operand == 6 ? $register_c
              :                 $operand;
            my $numerator   = $register_a;
            my $denominator = 2**$combo_operand;
            if ( $opcode == $INSTRUCTION_ADV ) {
                $register_a = int( $numerator / $denominator );
            }
            elsif ( $opcode == $INSTRUCTION_BDV ) {
                $register_b = int( $numerator / $denominator );
            }
            elsif ( $opcode == $INSTRUCTION_CDV ) {
                $register_c = int( $numerator / $denominator );
            }
            $instruction_pointer += 2;
        }
        elsif ( $opcode == $INSTRUCTION_BXL ) {
            my $operand = $program[ $instruction_pointer + 1 ];
            $register_b = $register_b ^ $operand;
            $instruction_pointer += 2;
        }
        elsif ( $opcode == $INSTRUCTION_BST ) {
            my $operand = $program[ $instruction_pointer + 1 ];
            my $combo_operand =
                $operand == 4 ? $register_a
              : $operand == 5 ? $register_b
              : $operand == 6 ? $register_c
              :                 $operand;
            $register_b = $combo_operand % 8;
            $instruction_pointer += 2;
        }
        elsif ( $opcode == $INSTRUCTION_JNZ ) {
            if ( $register_a == 0 ) {
                $instruction_pointer += 2;
            }
            else {
                my $operand = $program[ $instruction_pointer + 1 ];
                $instruction_pointer = $operand;
            }
        }
        elsif ( $opcode == $INSTRUCTION_BXC ) {
            my $operand = $program[ $instruction_pointer + 1 ];
            $register_b = $register_b ^ $register_c;
            $instruction_pointer += 2;
        }
        elsif ( $opcode == $INSTRUCTION_OUT ) {
            my $operand = $program[ $instruction_pointer + 1 ];
            my $combo_operand =
                $operand == 4 ? $register_a
              : $operand == 5 ? $register_b
              : $operand == 6 ? $register_c
              :                 $operand;
            push @out, $combo_operand % 8;
            $instruction_pointer += 2;
        }

    }

    return join q{,}, @out;
}

1;
