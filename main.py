def main():
    try:
        # Read the upper-right coordinates and exit if no input
        first_line = input().strip()
        if not first_line:
            print("Message: Provide a coordinate")
            return

        # Validate if grid size has a maximum coordinate of 50 
        max_x, max_y = map(int, first_line.split())        
        if max_x > 50 or max_y > 50:
            print("Error: Maximum coordinate value cannot exceed 50")
            return
        
        # Store lost robot positions (scent markers)
        scent_positions = set()
        
        # Process each robot
        while True:
            try:
                # Read robot initial position and orientation
                line = input().strip()
                if not line:
                    continue
                    
                parts = line.split()
                if len(parts) < 3:
                    continue
                    
                x, y, orientation = parts[0], parts[1], parts[2]
                x = int(x)
                y = int(y)
                
                if x > 50 or y > 50 or x < 0 or y < 0:
                    print(f"Error: Robot starting position ({x}, {y}) exceeds coordinate limits")
                    continue
                
                instructions = input().strip()
                
                # Validate instruction length is maximum character of 100
                if len(instructions) >= 100:
                    print("Error: Instruction string too long (max 100 characters)")
                    continue
                
                lost = False
                
                # Process each instruction
                for instruction in instructions:
                    if lost:
                        break

                    # Turn Left
                    if instruction == 'L':
                        if orientation == 'N':
                            orientation = 'W'
                        elif orientation == 'W':
                            orientation = 'S'
                        elif orientation == 'S':
                            orientation = 'E'
                        elif orientation == 'E':
                            orientation = 'N'

                    # Turn Right        
                    elif instruction == 'R':
                        if orientation == 'N':
                            orientation = 'E'
                        elif orientation == 'E':
                            orientation = 'S'
                        elif orientation == 'S':
                            orientation = 'W'
                        elif orientation == 'W':
                            orientation = 'N'
                    
                    # Move forward
                    elif instruction == 'F':
                        new_x, new_y = x, y
                        
                        if orientation == 'N':
                            new_y += 1
                        elif orientation == 'S':
                            new_y -= 1
                        elif orientation == 'E':
                            new_x += 1
                        elif orientation == 'W':
                            new_x -= 1
                        
                        # Check if new position is out of bounds
                        if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                            if (x, y) in scent_positions:
                                continue
                            else:
                                scent_positions.add((x, y))
                                lost = True
                        else:
                            x, y = new_x, new_y
                
                # Output result
                if lost:
                    print(f"{x} {y} {orientation} LOST")
                else:
                    print(f"{x} {y} {orientation}")
                    
            except EOFError:
                break
            except ValueError:
                print("Error: Invalid input format")
                break
                
    except EOFError:
        pass  # No input provided
    except ValueError:
        print("Error: Invalid grid coordinates")

if __name__ == "__main__":
    main()