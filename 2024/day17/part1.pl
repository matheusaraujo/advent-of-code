## no critic (Subroutines::ProhibitExcessComplexity)
## no critic (ControlStructures::ProhibitCascadingIfElse)
## no critic (RegularExpressions::RequireExtendedFormatting)

# TODO: @matheusaraujo - this code strongly needs refactoring

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

sub part1 {
    my @puzzle_input = @_;

    my $register_a = int( $puzzle_input[0] =~ s/Register A: //rsm );
    my $register_b = int( $puzzle_input[1] =~ s/Register B: //rsm );
    my $register_c = int( $puzzle_input[2] =~ s/Register C: //rsm );
    my @program    = split /,/smx, $puzzle_input[4] =~ s/Program: //rsm;
    my @out        = ();

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
