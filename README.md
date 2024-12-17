
MidEng 7.2 gRPC Framework [EK]

# Aufgabe

- Extend Requirements **überwiegend erfüllt**
  - Develop the Election client in another programming language
  - Document the new Election client

# GK:

[GitHub - IbimsderLukas/MidEng](https://github.com/IbimsderLukas/MidEng/tree/main)

# Aufgaben Lösung

Vote Client:

```python
request = vote_pb2.VoteRequest(VoteId="1")

    try:
        # Hole die Antwort vom Server
        response = stub.getVoteData(request)
        print(f"Vote ID: {response.VoteId}")
        for candidate in response.candidates:
            print(f"Candidate Name: {candidate.candidateName}, Votes: {candidate.votes}")
```

Request speichert die Antwort des Servers und gibt eine VoteID an. Dann wird mit response die Vote Data gespeichert und beim outprint verwendet.

Vote Server:

```py
response = vote_pb2.VoteResponse(
                VoteId=request.VoteId,
                candidates=[
                    vote_pb2.CandidateData(candidateName="Harald Hacker", votes=3000),
                    vote_pb2.CandidateData(candidateName="Sophie Schmidt", votes=2500)
                ]
            )
```

Die antwort die oben auch verwendet wird, besteht aus einem Array mit den Kandidaten und den Stimmen. Dies kann durch eine Datenbank zB ausgetauscht werden.

```py
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vote_pb2_grpc.add_VoteServiceServicer_to_server(VoteService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server starting on port 50051...")
```

Hier wird der Server erstellt auf Port 50051 und es wird ein Vote Service(Oben) hinzugefügt.

#
