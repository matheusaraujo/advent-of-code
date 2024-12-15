use strict;
use warnings;

sub part2 {
    my @puzzle_input = @_;

    my ( $x, $y, $seconds ) = ( 101, 103, 0 );
    my @robots = ();

    for my $line (@puzzle_input) {
        my ( $px0, $py0, $vx, $vy ) =
          $line =~ /p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)/sxm;

        push @robots, { x => $px0, y => $py0, vx => $vx, vy => $vy };
    }

    # Hide the cursor to prevent flickering
    print "\e[?25l";

    while (1) {
        my %positions = ();
        for my $robot (@robots) {
            my $px = ( $robot->{x} + $robot->{vx} * $seconds ) % $x;
            my $py = ( $robot->{y} + $robot->{vy} * $seconds ) % $y;

            $positions{"$px,$py"} = 1;
        }

        for my $j ( 0 .. $x - 1 ) {
            for my $i ( 0 .. $y - 1 ) {
                my $symbol = $positions{"$i,$j"} ? q{*} : q{.};

                # Move the cursor to the desired position and print the symbol
                print "\e[" . ( $j + 1 ) . ";" . ( $i + 1 ) . "H$symbol";
            }
        }

        if ( scalar keys %positions == scalar @robots ) {
            last;
        }
        $seconds++;
    }

    # Show the cursor again
    print "\e[?25h";

    return $seconds;
}

1;
