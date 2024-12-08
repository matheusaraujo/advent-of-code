use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;
    my $result       = 0;
    my $mul_enabled  = 1;
    foreach my $line (@puzzle_input) {
        my @matches =
          grep { defined } $line =~ /(mul|do|don't)[(](\d+)?,?(\d+)?[)]/sxmg;
        while (@matches) {
            my $match = shift @matches;
            if ( $match eq 'do' ) {
                $mul_enabled = 1;
            }
            elsif ( $match eq 'don\'t' ) {
                $mul_enabled = 0;
            }
            elsif ( $match eq 'mul' ) {
                my $a = shift @matches;
                my $b = shift @matches;
                if ($mul_enabled) {
                    $result += $a * $b;
                }
            }
        }
    }

    return $result;
}

1;

