# DialogTag

Dialogue act classification is the task of classifying an utterance with respect to the function it serves in a dialogue, i.e. the act the speaker is performing. This python library essentially does dialogue act classification on the Switchboard corpus.

The Switchboard-1 corpus is a telephone speech corpus, consisting of about 2,400 two-sided telephone conversation among 543 speakers with about 70 provided conversation topics. The dataset includes the audio files and the transcription files, as well as information about the speakers and the calls.
A subset of the Switchboard-1 corpus consisting of 1155 conversations was used. The resulting tags include dialogue acts like statement-non-opinion, acknowledge, statement-opinion, agree/accept, etc.

Annotated example:
>Speaker: A, Dialogue Act: Yes-No-Question, Utterance: So do you go to college right now?

The original dataset contained around 42 tags but here we brought them down to 38 by removing a few redundant and ad-hoc tags. The available tags:

| TAG                          | EXAMPLE                                           |
|------------------------------|---------------------------------------------------|
| Statement-non-opinion        | *Me, I'm in the legal department.*                |
| Acknowledge (Backchannel)    | *Uh-huh.*                                         |
| Statement-opinion            | *I think it's great*                              |
| Agree/Accept                 | *That's exactly it.*                              |
| Appreciation                 | *I can imagine.*                                  |
| Yes-No-Question              | *Do you have to have any special training?*       |
| Yes answers                  | *Yes.*                                            |
| Conventional-closing         | *Well, it's been nice talking to you.*            |
| Uninterpretable              | *But, uh, yeah*                                   |
| Wh-Question                  | *Well, how old are you?*                          |
| No answers                   | *No.*                                             |
| Response Acknowledgement     | *Oh, okay.*                                       |
| Hedge                        | *I don't know if I'm making any sense or not.*    |
| Declarative Yes-No-Question  | *So you can afford to get a house?*               |
| Other                        | *Well give me a break, you know.*                 |
| Backchannel in question form | *Is that right?*                                  |
| Quotation                    | *You can't be pregnant and have cats*             |
| Summarize/reformulate        | *Oh, you mean you switched schools for the kids.* |
| Affirmative non-yes answers  | *It is.*                                          |
| Action-directive             | *Why don't you go first*                          |
| Collaborative Completion     | *Who aren't contributing.*                        |
| Repeat-phrase                | *Oh, fajitas*                                     |
| Open-Question                | *How about you?*                                  |
| Rhetorical-Questions         | *Who would steal a newspaper?*                    |
| Hold before answer/agreement | *I'm drawing a blank.*                            |
| Negative non-no answers      | *Uh, not a whole lot.*                            |
| Signal-non-understanding     | *Excuse me?*                                      |
| Conventional-opening         | *How are you?*                                    |
| Or-Clause                    | *or is it more of a company?*                     |
| Dispreferred answers         | *Well, not so much that.*                         |
| 3rd-party-talk               | *My goodness, Diane, get down from there.*        |
| Offers, Options Commits      | *I'll have to check that out*                     |
| Self-talk                    | *What's the word I'm looking for*                 |
| Downplayer                   | *That's all right.*                               |
| Maybe/Accept-part            | *Something like that*                             |
| Tag-Question                 | *Right?*                                          |
| Declarative Wh-Question      | *You are what kind of buff?*                      |
| Apology                      | *I'm sorry.*                                      |
| Thanking                     | *Hey thanks a lot*                                |

## Installation

We recommend Python 3.7 or higher, Tensorflow 2.0.0 or higher and Transformers v3.0.0 or higher.

### Install with pip

Install the DialogTag with pip:

```
pip install -U DialogTag
```

### Install from sources

Alternatively, you can also clone the latest version from the repository and install it directly from the source code:

```
pip install -e .
```

## DialogTag in action

This quick example will show you how to use DialogTag in your code.
```
from dialog_tag import DialogTag

model = DialogTag('distilbert-base-uncased')

sentence = "I'll probably go to shopping today."
output = model.predict_tag(sentence)
print(output)
# output: 'Statement-non-opinion'

sentence = "Why are you asking me this question again and again?"
output = model.predict_tag(sentence)
print(output)
# output: 'Wh-Question'
```

## Available pre-trained models

Currently we have only distilbert-base-uncased available. We're planning to extend it to bert-base-uncased and roberta-base. Stay tuned for further updates!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details