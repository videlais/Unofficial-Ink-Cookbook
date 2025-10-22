require 'rouge'

module Rouge
  module Lexers
    class Ink < RegexLexer
      title "Ink"
      desc "Inkle's narrative scripting language"
      tag 'ink'
      filenames '*.ink'
      
      # Define token types
      state :root do
        # Comments
        rule %r{//.*$}, Comment::Single
        rule %r{/\*.*?\*/}m, Comment::Multiline
        
        # Knots (=== KnotName ===)
        rule %r{^(\s*)(===)(\s*)(function)?(\s*)(\w+)(\s*)(===)(\s*)$} do
          groups Text, Keyword, Text, Keyword, Text, Name::Function, Text, Keyword, Text
        end
        
        # Stitches (= StitchName)
        rule %r{^(\s*)(=)(\s+)(\w+)(\s*)$} do
          groups Text, Keyword, Text, Name::Label, Text
        end
        
        # Diverts (->)
        rule %r{(->)(\s*)(\w+(?:\.\w+)*)?} do
          groups Operator, Text, Name::Variable
        end
        
        # Choices (* and +)
        rule %r{^(\s*)([*+]+)(\s*)}, Generic::Prompt
        
        # Gathering points (-)
        rule %r{^(\s*)(-)(\s*)}, Generic::Prompt
        
        # Variables
        rule %r{\b(VAR|TEMP|CONST)\b}, Keyword::Declaration
        rule %r{\b(INCLUDE|EXTERNAL)\b}, Keyword::Namespace
        
        # Built-in functions
        rule %r{\b(POW|RANDOM|FLOOR|INT|FLOAT|CHOICE_COUNT|TURNS|SEED_RANDOM)\b}, Name::Builtin
        
        # Special knots
        rule %r{\b(DONE|END)\b}, Name::Constant
        
        # Logic operators
        rule %r{(\|\||&&|==|!=|<=|>=|<|>)}, Operator
        rule %r{(\+|\-|\*|/|%)}, Operator
        rule %r{(\?|:|!)}, Operator
        
        # Assignment and logic
        rule %r{(~|\=)}, Operator
        
        # Curly braces for logic
        rule %r/\{/, Punctuation, :logic
        
        # Square brackets for choice text
        rule %r/\[/, Punctuation, :choice_text
        
        # Parentheses for labels
        rule %r/\((\w+)\)/, Name::Label
        
        # Numbers
        rule %r{\b\d+(?:\.\d+)?\b}, Num
        
        # Strings
        rule %r{"[^"]*"}, Literal::String::Double
        rule %r{'[^']*'}, Literal::String::Single
        
        # Tags (# tagname)
        rule %r{#\s*\w+(?::\s*\w+)?}, Comment::Special
        
        # Whitespace (spaces, tabs, newlines)
        rule %r{\s+}, Text::Whitespace
        
        # Regular text and punctuation
        rule %r{[\w\p{P}]}, Text
        
        # Catch any remaining characters as text (not errors)
        rule %r{.}, Text
      end
      
      # Logic expressions inside { }
      state :logic do
        rule %r/\}/, Punctuation, :pop!
        rule %r{(not|and|or)\b}, Operator::Word
        rule %r{\b(true|false)\b}, Keyword::Constant
        rule %r{\b\w+\b}, Name::Variable
        rule %r{\b\d+(?:\.\d+)?\b}, Num
        rule %r{"[^"]*"}, Literal::String::Double
        rule %r{(\|\||&&|==|!=|<=|>=|<|>|\+|\-|\*|/|%|\?|:|!)}, Operator
        rule %r{(\(|\)|,)}, Punctuation
        rule %r{\s+}, Text::Whitespace
        rule %r{.}, Text
      end
      
      # Choice text inside [ ]
      state :choice_text do
        rule %r/\]/, Punctuation, :pop!
        rule %r{\s+}, Text::Whitespace
        rule %r{.}, Literal::String
      end
    end
  end
end